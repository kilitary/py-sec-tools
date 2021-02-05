rule _SimbiOZ__Extranger_vyocnz
{
	meta:
		description = "SimbiOZ __ Extranger"
	strings:
		$a = {5060E8000000005D81ED0710400068800B00008D851F10400050E8840B0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
