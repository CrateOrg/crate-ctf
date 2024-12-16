import { readFile, readdir, mkdir } from "node:fs/promises";
import { randomUUID } from "node:crypto";
import express from "express";
import fileUpload from "express-fileupload";
import cookieParser from "cookie-parser";

let cookieSecret = process.env.SECRET;

let app = express();
app.use(fileUpload({ limits: { fileSize: 1024 * 100, files: 1 }, abortOnLimit: true }));
app.use(cookieParser(cookieSecret));

/**
 * @param f {express.RequestHandler}
 * @returns {express.RequestHandler}
 */
function eh(f) {
    return (req, res, next) => {
        let r = f(req, res, next);
        if (r instanceof Promise) {
            r.catch(err => {
                console.error(err);
                res.status(500).send(err.message);
            });
        }
    };
}

app.use(eh(async (req, res, next) => {
    let cookies = new Map(req.headers.cookie?.split(/; ?/g)?.map(c => c.split("=").map(decodeURIComponent)));
    let session = cookieParser.signedCookie(cookies.get("session"), cookieSecret);
    if (session) {
        req.session = session;
    } else {
        let id = randomUUID();
        res.cookie("session", id, { signed: true });
        req.session = id;
        await mkdir(`./uploaded/${req.session}`);
    }
    next();
}));

app.get("/", eh(async (req, res) => {
    let entries = await readdir(`./uploaded/${req.session}`);
    res.send(`
        <!DOCTYPE html>
        <html lang="sv">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Fillagringstjänst™™</title>
        </head>
        <body>
            <h1>Fillagringstjänst™ - en tjänst som lagrar filer åt dig (det hade du aldrig kunnat gissa!)</h1>
            <ul>
                ${entries.map(entry => `<li><a href="/uploaded/${entry}">${entry}</a></li>`).join("")}
            </ul>
            <form action="/upload" method="post" encType="multipart/form-data">
                <input
                    onchange="if (this.files[0].size > 1024 * 100) {
                        alert('Filen får inte vara större än 100 KiB');
                        this.value = null;
                    }"
                    type="file"
                    name="file"
                    required
                >
                <button>Ladda upp</button>
            </form>
            <footer style="position: absolute; bottom: 1em">
                Fillagringstjänst™ är <a href="/src">öppen sås</a>!
            </footer>
        </body>
        </html>
    `);
}));

app.get("/src", eh(async(req, res) => {
    res.header("Content-Type", "text/plain");
    res.send(await readFile(import.meta.filename));
}));

app.post("/upload", eh(async (req, res) => {
    if (!req.files) return res.status(400).send("Missing file");
    let file = /** @type{fileUpload.UploadedFile} */ (req.files.file);
    if (!file) return res.status(400).send("Missing file");
    if (file.name.includes("/")) return res.status(400).send("Fippel förbjudet");
    await file.mv(`./uploaded/${req.session}/${file.name}`);
    res.redirect(303, "/");
}));

app.get("/uploaded/*", eh(async (req, res) => {
    let path = /** @type{string} */ (req.params[0]);
    if (path.includes("/")) return res.status(400).send("Fippel förbjudet");
    const contents = await readFile(`./uploaded/${req.session}/${path}`);
    res.send(contents);
}));

app.listen(2580, () => console.log("Listening for connections on port 2580"));
