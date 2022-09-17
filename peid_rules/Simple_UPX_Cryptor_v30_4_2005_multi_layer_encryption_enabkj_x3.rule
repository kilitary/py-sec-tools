rule _Simple_UPX_Cryptor_v30_4_2005_multi_layer_encryption_enabkj
{
	meta:
		description = "Simple UPX Cryptor v30_4_2005 _multi layer encryption"
	strings:
		$a = {60B8????????B8????????8A140880F2??8814084183F9??75F1}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
