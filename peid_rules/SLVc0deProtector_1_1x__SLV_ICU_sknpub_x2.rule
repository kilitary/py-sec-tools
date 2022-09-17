rule _SLVc0deProtector_1_1x__SLV_ICU_sknpub
{
	meta:
		description = "SLVc0deProtector 1_1x __ SLV  ICU"
	strings:
		$a = {E80000000058C600EBC6400108FFE0E94C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
