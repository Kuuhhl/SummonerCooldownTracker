# SummonerCooldownTracker
This project aims to help you and your allys keep track of enemy summoner cooldowns in League of Legends.

To do this, it uses text-recognition to read your ping message in Chat.


It calculates the time the spell will be up again and writes it into chat (e.g. 'Lee Sin has no flash until 5:31.').

This is especially useful to let your jungler plan better gank timings and also for yourself to know how long you will have the advantage.
## Disclaimer
This is a work in progress and doesn't work reliably yet. If you are interested in helping, you're welcome to open a pull request.
# TODO
- Improve text recognition (Train OCR algorithm on font)
- Fetch spell cooldowns from DDragon API instead of hard-coding
- Adding support for Ultimate Abilities (e.g. Kayle has no Ultimate until 20:14.)
- Writing a message when spell is up again (e.g. Kayle has Ultimate again!)
# Will I get banned for using this tool?
As this tool doesn't manipulate any game files or read memory, it should not get detected by Riot.
