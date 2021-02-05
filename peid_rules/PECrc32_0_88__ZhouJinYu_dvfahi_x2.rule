rule _PECrc32_0_88__ZhouJinYu_dvfahi
{
	meta:
		description = "PECrc32 0_88 __ ZhouJinYu"
	strings:
		$a = {60E8000000005D81ED????????B9????00008DBD????????8BF7AC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
