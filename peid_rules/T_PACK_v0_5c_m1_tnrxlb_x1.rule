rule _T_PACK_v0_5c_m1_tnrxlb
{
	meta:
		description = "T_PACK v0_5c _m1"
	strings:
		$a = {68????FD60BE????BF????B9????F3A48BF7BF????FC46E98EFE}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
