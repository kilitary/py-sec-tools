rule _Zortech_C_ibiwhm
{
	meta:
		description = "Zortech C"
	strings:
		$a = {E8????2EFF??????FC06}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
