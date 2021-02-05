rule _UPX_v0_89_6__v1_02_v1_05__v1_22_DLL_hqwusd
{
	meta:
		description = "UPX v0_89_6 _ v1_02  v1_05 _ v1_22 DLL"
	strings:
		$a = {807C2408010F85??????0060BE????????8DBE????????5783CDFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
