rule _SLVc0deProtector_0_60__SLV_ICU_hijnuc
{
	meta:
		description = "SLVc0deProtector 0_60 __ SLV  ICU"
	strings:
		$a = {EB02FA04E84900000069E84900000095E84F00000068E81F00000049E8E9FFFFFF67E81F00000093E83100000078E8DD}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
