rule _PE_PACK_1_0_nhdysx
{
	meta:
		description = "PE_PACK 1_0"
	strings:
		$a = {7400E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
