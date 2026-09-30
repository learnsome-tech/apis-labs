# Contributing

Thank you for helping make these labs better.

## Report a problem

Open an issue: [a lab is broken](../../issues/new?template=lab-broken.yml), or [something in a lab or lesson is wrong](../../issues/new?template=content-error.yml). Include the lab id (for example `m01l01-02`), what you ran and the output of `./check <lab>`. A problem with your LearnSome.tech account or billing goes to https://learnsome.tech/support, not here.

## Pull requests

Everything in this repository is generated from the LearnSome.tech course: the lab files, the READMEs, `./check`, the dev container and the workflows. The generator rewrites all of it whenever the course changes, so a pull request that edits a generated file would be overwritten. Please open an issue instead: we fix the course, and the fix reaches this repository with the next update.

## Checking a change locally

`./check --lint` runs what CI runs: every lab has its README, its check configuration and, when it is graded, its expected output, and the starters parse. `./check <lab>` runs a lab the way the site does.

## Conduct

Be kind and specific. Issues are for the labs and their content; keep personal details and solutions to the lesson exercises out of them.
