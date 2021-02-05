rule _Packman_0_0_0_1__bubba_tpovyw
{
	meta:
		description = "Packman 0_0_0_1 __ bubba"
	strings:
		$a = {60E800000000588DA8??FEFFFF8D98??????FF8D????010000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
