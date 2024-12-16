import puppeteer from "puppeteer";

const [_node, _script, username, password] = process.argv;

(async () => {
    const browser = await puppeteer.launch({ headless: "new" });
    const page = await browser.newPage();
    await page.goto("http://web:3000");
    const registerLink = await page.waitForSelector('a[href="/register"]');
    registerLink.click();

    const usernameInput = await page.waitForSelector('input[name="username"]');
    const passwordInput = await page.waitForSelector('input[name="password"]');
    const registerButton = await page.waitForSelector('form button');

    await usernameInput.focus();
    await page.keyboard.type(username);
    await passwordInput.focus();
    await page.keyboard.type(password);
    await registerButton.click();

    await new Promise(res => setTimeout(res, 1000));
    process.exit(0);
})().catch(console.error);
