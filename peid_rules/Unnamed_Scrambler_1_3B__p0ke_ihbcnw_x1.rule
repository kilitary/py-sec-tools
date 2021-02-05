rule _Unnamed_Scrambler_1_3B__p0ke_ihbcnw
{
	meta:
		description = "Unnamed Scrambler 1_3B __ p0ke"
	strings:
		$a = {558BECB9050000006A006A004975F951535657B8??3A????E8??ECFFFF33C05568????????64FF30648920E8??D7FFFFE8????FFFFB820??????33C9BA04010000E8??DBFFFF68040100006820??????6A00FF1510}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
