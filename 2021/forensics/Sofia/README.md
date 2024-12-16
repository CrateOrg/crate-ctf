# Sofia
XP-maskin som kör lite processer, surfar, osv och har ascii-art-text i notepad som går att extrahera
ut med exempelvis volatility.

## Volatility som docker:
docker pull phocean/volatility
function volatility() { docker run --rm --user=$(id -u):$(id -g) -v "$(pwd)":/dumps -ti phocean/volatility $@; }

## Dumpa minne
VBoxManage.exe debugvm "xpchall" dumpvmcore --filename dump.elf
Raw-dumpen i utmaningen är dock gjord med winpmem 1.6.2 inifrån VM:en och sedan utflyttad

## Hitta profile:
volatility -f /dumps/dump.raw imageinfo

## Lista processer
volatility -f /dumps/dump.raw --profile WinXPSP3x86 pslist

## Dumpa notepad info:
volatility -f /dumps/dump.raw --profile WinXPSP3x86 notepad


