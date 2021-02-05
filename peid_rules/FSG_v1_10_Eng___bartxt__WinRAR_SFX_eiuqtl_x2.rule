rule _FSG_v1_10_Eng___bartxt__WinRAR_SFX_eiuqtl
{
	meta:
		description = "FSG v1_10 _Eng_ __ bartxt __ WinRAR_SFX"
	strings:
		$a = {061E0E0E071FB430CD2186E03D000373??CD20EB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
