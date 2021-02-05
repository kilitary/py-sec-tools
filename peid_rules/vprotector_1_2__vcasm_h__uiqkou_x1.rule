rule _vprotector_1_2__vcasm_h__uiqkou
{
	meta:
		description = "vprotector 1_2 __ vcasm _h_"
	strings:
		$a = {558BEC6AFF68????????68????????64A1000000005064892500000000E803000000C7840058EB01E983C00750C3FF35E803000000C7840058EB01E983C00750C3FF35E807000000C78383C013EB0B58EB02CD2083}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
