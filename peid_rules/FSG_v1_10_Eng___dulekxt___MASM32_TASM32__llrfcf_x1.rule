rule _FSG_v1_10_Eng___dulekxt___MASM32_TASM32__llrfcf
{
	meta:
		description = "FSG v1_10 _Eng_ __ dulekxt __ _MASM32  TASM32_"
	strings:
		$a = {03F723FE33FBEB02CD20BB80??4000EB0186EB0190B8F400000083EE052B}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
