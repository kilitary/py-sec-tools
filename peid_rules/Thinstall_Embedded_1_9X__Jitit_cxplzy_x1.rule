rule _Thinstall_Embedded_1_9X__Jitit_cxplzy
{
	meta:
		description = "Thinstall Embedded 1_9X __ Jitit"
	strings:
		$a = {558BEC515356576A006A00FF15????????50E887FCFFFF5959A1????????8B40100305????????8945FC8B45FCFFE05F5E5BC9C3000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
