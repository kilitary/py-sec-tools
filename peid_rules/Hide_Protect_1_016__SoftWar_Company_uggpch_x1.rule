rule _Hide_Protect_1_016__SoftWar_Company_uggpch
{
	meta:
		description = "Hide_Protect 1_016 __ SoftWar Company"
	strings:
		$a = {909090E9D8??050095??5300954A5000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
