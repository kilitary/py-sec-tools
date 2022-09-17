rule _VProtector_V1_0B__vcasm_rspwvh
{
	meta:
		description = "VProtector V1_0B __ vcasm"
	strings:
		$a = {558BEC6AFF68CA374100680638410064A1000000005064892500000000E803000000C7840058EB01E983C00750}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
