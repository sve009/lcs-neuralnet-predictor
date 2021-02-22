my_lines = []

with open('data.txt', 'r') as reader:
    lines = reader.readlines()

    for line in lines:
        words = line.split('\t')
        if len(words) < 21:
            continue 
        while '%' not in words[0]:
            words.pop(0)
            if len(words) == 0:
                lines = lines.remove(line)
                break
        
        words[0] = str(float(words[0][:len(words[0]) - 2]) / 100.0)
        words[2] = str(float(words[2]) / 1000.0)
        
        (m, _, s) = words[4].partition(':')
        t = float(m) + (float(s) / 60.0)
        words[4] = str(t)

        words[17] = str(float(words[17]) / 1000.0)
        words[21] = str(float(words[21]) / 1000.0)

        temp_str = words[0]
        for word in words[1:]:
            temp_str = temp_str + "," + word
        my_lines.append(temp_str)


with open('formatted_data.csv', 'w') as writer:
    writer.write('"Win Rate","K:D","GPM","GDM","Game Duration","Kills/Game","Deaths/Game","Towers Killed","Towers Lost","FB%","FT%","DRAPG","DRA%","HERPG","Her%","DRA@15","TD@15","GD@15","NASHPG","NASH%","CSM","DPM","WPM","VWPM","WCPM"\n')
    writer.writelines(my_lines)
