rule _Unknown_UPX_modifyer_jyxwyw
{
	meta:
		description = "Unknown UPX modifyer"
	strings:
		$a = {E802000000CD035A81C2????????81C2????????89D181C13C05000052812A3353451283C20439CA7EF389CA8B42048D182902BB7856000083EA043B14247DECC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
