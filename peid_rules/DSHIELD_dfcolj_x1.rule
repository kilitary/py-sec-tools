rule _DSHIELD_dfcolj
{
	meta:
		description = "DSHIELD"
	strings:
		$a = {06E8????5E83EE??16179C58B9????25????2E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
