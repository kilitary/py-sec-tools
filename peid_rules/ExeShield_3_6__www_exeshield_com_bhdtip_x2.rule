rule _ExeShield_3_6__www_exeshield_com_bhdtip
{
	meta:
		description = "ExeShield 3_6 __ www_exeshield_com"
	strings:
		$a = {B8??????005064FF35000000006489250000000033C089085045436F6D706163743200CE1E42AFF8D6CCE9FBC84F1B227CB4C80DBD71A9C81F5FB1298F11738F00D18887A93F4D006C3CBFC080F7AD3523EB84826F}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
