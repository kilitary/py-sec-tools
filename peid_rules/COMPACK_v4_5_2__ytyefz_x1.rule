rule _COMPACK_v4_5_2__ytyefz
{
	meta:
		description = "COMPACK v4_5 _2_"
	strings:
		$a = {BE????E8????5D83????55505351520E070E1F8BCE}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
