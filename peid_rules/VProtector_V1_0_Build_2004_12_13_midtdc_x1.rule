rule _VProtector_V1_0_Build_2004_12_13_midtdc
{
	meta:
		description = "VProtector V1_0 _Build 2004_12_13"
	strings:
		$a = {558BEC6AFF681A894000685689400064A1000000005064892500000000E803000000C7840058EB01E983C00750}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
