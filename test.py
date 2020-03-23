def main():
    for i in range(0, len(pro_links_list), 1):
        all_t = []
        twenty_records = pro_links_list[i:i + 1]
        for record_arg in twenty_records:
            try:
                pdg = ProductDescriptionGetter(record_arg)
                t = threading.Thread(target=pdg.start)
                t.start()
                all_t.append(t)
            except Exception as error:
                print(f"Error in starting thread ==> {error}")
        for count, t in enumerate(all_t):
            print(f"joining Thread no ==> {count}")
            t.join()




            