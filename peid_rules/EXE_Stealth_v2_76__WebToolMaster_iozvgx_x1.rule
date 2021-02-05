rule _EXE_Stealth_v2_76__WebToolMaster_iozvgx
{
	meta:
		description = "EXE Stealth v2_76 __ WebToolMaster"
	strings:
		$a = {EB65457865537465616C7468205632202D207777772E776562746F6F6C6D61737465722E636F6D20594F55522041442048455245215069524143592069532041}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
