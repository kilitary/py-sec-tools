rule _BeRoEXEPacker_v1_00_DLL_LZBRS_xwrkjy
{
	meta:
		description = "BeRoEXEPacker v1_00 DLL _LZBRS"
	strings:
		$a = {837C2408010F85????????60BE????????BF????????FCAD8D1C07B0803BFB733BE81C0000007203A4EBF2E81A0000008D51FFE812000000568BF72BF2F3A45EEBDB02C07503AC12C0C333}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
