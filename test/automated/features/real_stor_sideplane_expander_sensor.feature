Feature: Test Sideplane Expander Sensor Capabilities
	Send Sideplane Expander sensor request messages to SSPL and
	verify the response messages contain the correct information.

Scenario: Send SSPL a sideplane expander sensor message requesting sideplane expander data
	Given that SSPL is running
	When I send in the sideplane expander sensor message to request the current "enclosure_sideplane_expander_alert" data
	Then I get the sideplane expander sensor JSON response message
