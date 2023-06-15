# Mac

mac-monitor-start:
	@docker-compose -f docker-compose-mac.yml up -d

mac-monitor-build:
	@docker-compose -f docker-compose-mac.yml build

mac-monitor-down:
	@docker-compose -f docker-compose-mac.yml down

# RPi

monitor-start:
	@docker-compose -f docker-compose.yml up -d

monitor-build:
	@docker-compose -f docker-compose.yml build

monitor-down:
	@docker-compose -f docker-compose.yml down