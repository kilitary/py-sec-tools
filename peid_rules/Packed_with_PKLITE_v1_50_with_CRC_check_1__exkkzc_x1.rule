rule _Packed_with_PKLITE_v1_50_with_CRC_check_1__exkkzc
{
	meta:
		description = "Packed with_ PKLITE v1_50 with CRC check _1_"
	strings:
		$a = {1FB409BA????CD21B8????CD21}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
