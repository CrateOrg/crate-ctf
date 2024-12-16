import puppeteer from "puppeteer";
import { createHash } from "crypto";

const [_node, _script, username, unhashedPassword] = process.argv;

const password = createHash("sha256").update(unhashedPassword).digest("hex");

(async () => {
    const browser = await puppeteer.launch({ headless: "new" });
    const page = await browser.newPage();
    await page.goto("http://web:3000");
    const loginLink = await page.waitForSelector('a[href="/login"]');
    loginLink.click();

    {
        const usernameInput = await page.waitForSelector('input[name="username"]');
        const passwordInput = await page.waitForSelector('input[name="password"]');
        const loginButton = await page.waitForSelector('form button');

        await passwordInput.focus();
        await page.keyboard.type(username);
        await usernameInput.focus();
        await page.keyboard.type(password);
        await loginButton.click();
    }

    await new Promise(res => setTimeout(res, 10000));

    {
        const usernameInput = await page.waitForSelector('input[name="username"]');
        const passwordInput = await page.waitForSelector('input[name="password"]');
        const loginButton = await page.waitForSelector('form button');

        await usernameInput.focus();
        await usernameInput.click({ count: 3 });
        await page.keyboard.type(username);
        await passwordInput.focus();
        await page.keyboard.type(password);
        await loginButton.click();
    }

    await new Promise(res => setTimeout(res, 1000));
    process.exit(0);
})().catch(console.error);
