import puppeteer from "puppeteer";

const [_node, _script, username, password] = process.argv;

(async () => {
    const browser = await puppeteer.launch({ headless: "new" });
    const page = await browser.newPage();
    await page.goto("http://web:3000");
    const loginLink = await page.waitForSelector('a[href="/login"]');
    loginLink.click();

    const usernameInput = await page.waitForSelector('input[name="username"]');
    const passwordInput = await page.waitForSelector('input[name="password"]');
    const loginButton = await page.waitForSelector('form button');

    await usernameInput.focus();
    await page.keyboard.type(username);
    await passwordInput.focus();
    await page.keyboard.type(password);
    await loginButton.click();

    await new Promise(res => setTimeout(res, 3000));
    for (let i = 0; i < 3; i++) {
        await page.$$eval("button", buttons => buttons[Math.floor(Math.random() * buttons.length)].click());
        await new Promise(res => setTimeout(res, 10000));
    }

    process.exit(0);
})().catch(console.error);
