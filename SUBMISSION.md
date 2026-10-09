# Submission checklist

- [ ] GitHub repo link (public), README visible
- [ ] Actions tab: green runs for test and docker-build (screenshot)
- [ ] Live URL `/health` and `/docs` with the elasticbeanstalk.com address visible (screenshot)
- [ ] Dashboard: HIGH risk result, "Backend online" badge (screenshot)
- [ ] AI Diagnosis result on the live URL (after `eb setenv`) (screenshot)
- [ ] `docs/architecture.svg` included
- [ ] 2-minute demo video

## Demo script (2 minutes)
1. Show the architecture picture (10s).
2. Dashboard: "Healthy release" -> LOW.
3. "Unhealthy deployment" -> HIGH, score 100.
4. AI Diagnosis tab -> run it, read the first investigation step.
5. History tab, then the Actions tab with green runs.
6. Mention honestly: risk engine tested; CloudWatch and rollback logic unit-tested, live-AWS verification in progress.

## Claims you may make only when true
- "Dockerized": when the docker-build job is green.
- "Live metrics": after /metrics/live returns real data from your environment.
- "Rollback works": after you tested it on a real environment.
