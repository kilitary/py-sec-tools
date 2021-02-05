rule _SimbiOZ_PolyCryptor_v_xx__Extranger_gfnfqg
{
	meta:
		description = "SimbiOZ PolyCryptor v_xx__ Extranger"
	strings:
		$a = {5560E8000000005D81ED????????8D85????????68????????50E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
