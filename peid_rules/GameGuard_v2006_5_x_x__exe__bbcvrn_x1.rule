rule _GameGuard_v2006_5_x_x__exe__bbcvrn
{
	meta:
		description = "GameGuard v2006_5_x_x ___exe_"
	strings:
		$a = {31FF740661E94A4D50305ABA7D000000807C240801E90000000060BE00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
