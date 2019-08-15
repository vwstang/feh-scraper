# Fire Emblem Heroes Game Data Scraper

Scrapes Gamepedia (and potentially Gamepress in the future) pages for list of heroes and their game stats and data.

Output in JSON.

Check out [feh-core-service](https://github.com/vwstang/feh-core-service) for a GraphQL server that serves this JSON output through an endpoint.

## Getting Started

```
pipenv sync
pipenv run python feheromanager.py
```

## Future Plans

For use in a future release of an Ally management app.
