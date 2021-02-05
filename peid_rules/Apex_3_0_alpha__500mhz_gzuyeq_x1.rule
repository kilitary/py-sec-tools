rule _Apex_3_0_alpha__500mhz_gzuyeq
{
	meta:
		description = "Apex 3_0 alpha __ 500mhz"
	strings:
		$a = {5FB91400000051BE00104000B900????008A07300646E2FB4759E2EA68??????00C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
