.DEFAULT_GOAL := help
IMAGE := ministryofjustice/tech-docs-github-pages-publisher:v4.0.0


.PHONY: preview
preview: ## Run a local instance of the documentation site, while editing
	docker run --platform=linux/amd64 --rm \
		-v $$(pwd)/config:/app/config \
		-v $$(pwd)/source:/app/source \
		-v $$(pwd)/scripts:/scripts \
		-p 4567:4567 \
		-it $(IMAGE) /scripts/preview.sh

.PHONY: report
report: ## Review which pages have expired
	 ./report-for-daniel-the-manual-spaniel.sh | tee expired_report_$$(date +"%F").txt

help:
	@grep -h -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
