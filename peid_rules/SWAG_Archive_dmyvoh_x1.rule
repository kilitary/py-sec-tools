rule _SWAG_Archive_dmyvoh
{
	meta:
		description = "SWAG Archive"
	strings:
		$a = {????2D7377312D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
