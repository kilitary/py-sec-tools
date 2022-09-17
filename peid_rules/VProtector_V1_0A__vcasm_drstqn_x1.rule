rule _VProtector_V1_0A__vcasm_drstqn
{
	meta:
		description = "VProtector V1_0A __ vcasm"
	strings:
		$a = {558BEC6AFF688A8E400068C68E400064A1000000005064892500000000E803000000C7840058EB01E983C00750}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
