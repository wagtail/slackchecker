import os
import requests

r = requests.head("https://wagtail.org/slack", headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}, allow_redirects=True)
if r.url.startswith('https://wagtailcms.slack.com/join/shared_invite/'):
    print("Slack invitation link is OK")
else:
    print("Slack invitation link has expired")

    if "SLACK_WEBHOOK_URL" in os.environ:
        print("Reporting to #nightly-build-failures slack channel")
        response = requests.post(
            os.environ["SLACK_WEBHOOK_URL"],
            json={
                "text": "Slack invitation link has expired. Please generate a new one and set it as the /slack redirect on wagtail.org",
            },
        )

        print(f"Slack responded with: {response}")

    else:
        print(
            "Unable to report to #nightly-build-failures slack channel because SLACK_WEBHOOK_URL is not set"
        )
