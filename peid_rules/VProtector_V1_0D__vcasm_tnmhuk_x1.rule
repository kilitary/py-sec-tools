rule _VProtector_V1_0D__vcasm_tnmhuk
{
	meta:
		description = "VProtector V1_0D __ vcasm"
	strings:
		$a = {558BEC6AFF68CA314100680632410064A1000000005064892500000000E803000000C7840058EB01E983C00750}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
