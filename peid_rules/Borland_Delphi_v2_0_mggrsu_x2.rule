rule _Borland_Delphi_v2_0_mggrsu
{
	meta:
		description = "Borland Delphi v2_0"
	strings:
		$a = {06FC8CC8BA????03D052BA????52BA????03C28BD805????8EDB8EC033F633FFB9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
