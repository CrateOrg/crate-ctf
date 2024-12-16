# Crate-CTF Challenge Repository
Welcome to the Crate-CTF challenge repository! This repository contains past Capture-The-Flag (CTF) challenges used in Crate-CTF, an annual cybersecurity competition organized by the Swedish Defense Research Agency (FOI).

Crate-CTF typically runs for 8 hours on an autumn Saturday. Participants solve a variety of challenges related to e.g. cryptography, reverse-engineering, or forensics. The competition aims to be both fun and to encourage learning.

For more information about Crate-CTF, visit the [FOI website](https://www.foi.se/cratectf).

## Table of Contents
- [About the Challenges](#about-the-challenges)
- [Repository Structure](#repository-structure)
- [Previous Competitions and Winners](#previous-competitions-and-winners)
- [Contact](#contact)
- [License](#license)

## About the Challenges
Each challenge in this repository was previously featured in the Crate-CTF competition. They are placed in one of the following categories:
- Cryptography
- Reverse engineering
- Web application security
- Forensics
- Exploit development
- Open Source Intelligence
- Miscellaneous (i.e. anything not fitting the above)

These challenges are provided for educational and practice purposes. It should be noted that the challenges are normally written in the swedish language.

## Repository Structure
The repository is organized by year. For each year the challenges are sorted into categories. The structure typically looks like this:
```
.
├── 2024
│   ├── README.md
│   ├── facit.md
│   ├── crypto
│   │   ├── CryptoChall_1
│   │   │   ├── challenge.yml
│   │   │   ├── README.md
│   │   │   ├── solve.py
│   │   │   ├── docker
│   ├── web
│   ├── ...
├─ 2023/
│  ├─ ...
└─ ...
```
- **Year directories**: Contain challenges for that particular year.
- **facit.md**: Contain a short solution text (in swedish) for each challenge.
- **Category directories**: Group challenges by topic, such as `crypto`, `reverse`, `web`, etc.
- **README.md**: Each challenge directory ideally includes a README detailing the challenge as well as a solution description.

## Previous Competitions and Winners
### 2024
1. [RoyalRoppers](https://royalroppers.team)
2. [KebabEngineers](https://kebab.team)
3. 5ca5dd

Alongside the competition was also an 8-hour long live-stream, featuring tutorials on previous challenges, a talk on OSINT, dial-in remote C64-gaming and much more. It can be found on [YouTube](https://www.youtube.com/live/edTmaN4lILw).

### 2023 
1. [KebabEngineers](https://kebab.team)
2. 5ca5dd
3. [RoyalRoppers](https://royalroppers.team)

### 2022 
1. [RoyalRoppers](https://royalroppers.team)
2. [watevr](https://watevr.xyz)
3. 5ca5dd

### 2021
1. [watevr](https://watevr.xyz)
2. KTHCTF0x1
3. 5ca5dd

### 2020
1. [watevr](https://watevr.xyz)
2. LionHack
3. KTHCTF0x1

## Contact
For questions, feedback, or general inquiries, please contact us at [cratectf@foi.se](mailto:cratectf@foi.se).  
We have a [Discord server](https://discord.gg/kUg6JQ62pJ), though it’s quieter outside competition periods. Crate-CTF can also be found on [CTFtime](https://ctftime.org/team/352250).

## License
The content in this repository is released under the MIT License unless otherwise stated. Please see the LICENSE file for details.
