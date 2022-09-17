rule _FSG_v2_0_gdmfqu
{
	meta:
		description = "FSG v2_0"
	strings:
		$a = {8725??????00619455A4B680FF13}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
