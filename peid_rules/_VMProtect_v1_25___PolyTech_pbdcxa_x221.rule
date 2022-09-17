rule __VMProtect_v1_25___PolyTech_pbdcxa
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????668B06988D760283ED04894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
