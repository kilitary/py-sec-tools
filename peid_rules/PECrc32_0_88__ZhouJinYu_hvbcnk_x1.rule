rule _PECrc32_0_88__ZhouJinYu_hvbcnk
{
	meta:
		description = "PECrc32 0_88 __ ZhouJinYu"
	strings:
		$a = {60E8000000005D81EDB6A445008DBDB0A4450081EF82000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
