rule _UPX_v0_71_DLL_sbotqc
{
	meta:
		description = "UPX v0_71 _DLL"
	strings:
		$a = {807C2408010F859501000060E80000000083}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
