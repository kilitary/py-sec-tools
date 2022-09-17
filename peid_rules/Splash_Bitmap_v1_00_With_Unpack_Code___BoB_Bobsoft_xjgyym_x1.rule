rule _Splash_Bitmap_v1_00_With_Unpack_Code___BoB_Bobsoft_xjgyym
{
	meta:
		description = "Splash Bitmap v1_00 _With Unpack Code_ ___ BoB  Bobsoft"
	strings:
		$a = {E800000000608B6C24205581ED????????8DBD????????8D8D????????29F931C0FCF3AA8B042448662500F06681384D5A75F48B483C813C015045000075E88985????????6A40}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
