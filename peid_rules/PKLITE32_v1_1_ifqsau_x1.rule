rule _PKLITE32_v1_1_ifqsau
{
	meta:
		description = "PKLITE32 v1_1"
	strings:
		$a = {68????????68????????6800000000E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
